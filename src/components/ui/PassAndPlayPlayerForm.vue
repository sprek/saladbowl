<v-dialog v-model="passPlayerDialog" max-width="600px">
<template>
  <v-card>
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
    <v-flex xs5>
      <v-btn block class="mt-3" @click.native="dialog = false">Cancel</v-btn>
    </v-flex>
    <v-flex xs2></v-flex>
    <v-flex xs5>
      <v-btn block class="mt-3" @click.stop="submitWords">Submit</v-btn>
    </v-flex>
    
    
  </v-layout>
</v-container>
</v-card>
</template>


<script>
import { mapState } from 'vuex';

export default {
  name: 'pass-and-play-player-form',
  data() {
    return {
      curColor: '',
      numWordsPerPlayer: 3,
      wordFields: [],
      valid: false,
      reqUsername: '',
      reqColor: '',
    };
  },
  computed: {
    ...mapState(['room_id',' game', 'ordered_players']),
    playerColor: function() {
      if (this.curColor == '') {
        var last_color = this.ordered_players[this.ordered_players.length-1].team
        if (last_color == 'blue') {
          return 'red'
        }
        return 'blue'
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
    submitWords() {
      if (!this.valid) {
        return;
      }

      console.log(`${this.wordFields.join(';')}`);
      console.log(`${this.wordFields.length}`);

      const remove_chars = this.wordFields.map((e) => {
        // get rid of semicolons, since we'll be using them to separate the entries
        const n = e.replace(/;/g, '');
        return n;
      });

      const params = {
        room_id: this.room_id,
        username: this.username,
        word_list: remove_chars.join(';'),
      };
      this.$socket.emit('submit_words', params);
    },
    changeTeam() {
      if (this.curColor == 'red') {
        this.curColor='blue';
      } else {
        this.curColor='red';
      }
    },
  },
};
</script>
<style>
</style>
