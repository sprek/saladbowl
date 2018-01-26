<template>
<v-card>
  <v-toolbar style="flex: 0 0 auto;" dark class="primary">
    <v-btn icon @click.native="cancelClick" dark>
      <v-icon>close</v-icon>
    </v-btn>
    <v-toolbar-title>Add Pass and Play Player</v-toolbar-title>
  </v-toolbar>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 text-xs-center>
        <v-btn label :color="playerColor" @click.stop="changeTeam"><h4>Team {{playerColor}}</h4></v-btn>
      </v-flex>
      <v-flex xs12 text-xs-center>
        <h5>Click to change</h5>
      </v-flex>
      <v-flex xs12>
        <v-form v-model="valid">
          <v-flex xs-8></v-flex>
          <v-text-field v-model="reqUsername" label="Username" required :rules="[v => !!v || 'Item is required']"></v-text-field>
          
          <template v-for="n in numWordsPerPlayer">
            <v-text-field v-model="wordFields[n-1]" label="Enter Word or Phrase" required :rules="[v => !!v || 'Item is required']"></v-text-field>
          </template>
        </v-form>
      </v-flex>
      <v-flex xs12>
        <v-btn block class="mt-3" @click.stop="submitWords">Submit</v-btn>
      </v-flex>
      
      
    </v-layout>
  </v-container>
</v-card>
</template>


<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'pass-and-play-player-form',
  data() {
    return {
      curColor: '',
      numWordsPerPlayer: 3,
      wordFields: [],
      valid: false,
      reqUsername: '',
    };
  },
  computed: {
    ...mapState(['room_id', 'nextColor', 'showAddPlayerDialog']),
    playerColor: function() {
      if (this.curColor == '') {
        this.curColor = this.nextColor;
        return this.nextColor;
      }
      else {
        return this.curColor;
      }
    }
  },
  watch: {
    game() {
      // console.log ("REQ USERNAME IS: " + this.reqUsername);
      // console.log ("SETTING ROOM ID: " + this.room_id);
      // this.set_username(this.reqUsername);
      // this.$router.push({name: 'Game', params: {room_id: this.room_id } });
    },
  },
  methods: {
    ...mapMutations(['set_showAddPlayerDialog']),
    submitWords() {
      if (!this.valid) {
        return;
      }
      const remove_chars = this.wordFields.map((e) => {
        // get rid of semicolons, since we'll be using them to separate the entries
        const n = e.replace(/;/g, '');
        return n;
      });
      
      const params = {
        room_id: this.room_id,
        username: this.reqUsername,
        word_list: remove_chars.join(';'),
        team: this.playerColor,
      };
      this.$socket.emit('submit_pass_and_play_player', params);
      this.set_showAddPlayerDialog(false);
    },
    changeTeam() {
      if (this.curColor == 'red') {
        this.curColor='blue';
      } else {
        this.curColor='red';
      }
    },
    cancelClick() {
      this.set_showAddPlayerDialog(false);
      //this.$emit('dclose');
    },
  },
};
</script>
<style>
</style>
