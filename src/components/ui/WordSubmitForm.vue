<template>
<v-card>
  <v-card-text>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <v-form v-model="valid">
          <template v-for="n in numWordsPerPlayer">
            <v-text-field v-model="wordFields[n]" label="Enter Word or Phrase" required :rules="[v => !!v || 'Item is required']"></v-text-field>
          </template>
          </v-form>
       </v-flex>
        <v-flex xs12>
          <v-btn block class="mt-3" @click.stop="submitWords">Submit</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card-text>
</v-card>
</template>

<script>
import { mapState, mapMutations} from 'vuex';
export default {
  name: 'word-submit-form',
  data() {
    return {
      numWordsPerPlayer: 3,
      wordFields: [],
      valid: false,
    };
  },
  computed: {
    ...mapState(['room_id', 'username', 'game']),
  },
  watch: {
    game() {
      //console.log ("REQ USERNAME IS: " + this.reqUsername);
      //console.log ("SETTING ROOM ID: " + this.room_id);
      //this.set_username(this.reqUsername);
      //this.$router.push({name: 'Game', params: {room_id: this.room_id } });
    },
  },
  methods: {
    submitWords() {
      if (!valid) {
        return;
      }
      
      var remove_chars = word_list.map(function(e) {
        e = e.replace(/,"/g,'');
        return e;
      });
      const params = {
        room_id: this.room_id
        username: this.username,
        word_list: this.remove_chars.join(',')
      }
      this.$socket.emit('submit_words', params);
    }
    //...mapMutations(['set_username']),
    //createGame() {
    //  console.log ("CREATING GAME WITH: " + this.reqUsername + ", " + this.numWordsPerPlayer);
    //  const params = {
    //    username: this.reqUsername,
    //    numWordsPerPlayer: this.numWordsPerPlayer,
    //  };
    //  this.$socket.emit('create', params);
    //}
  }
}
</script>
<style>
</style>
