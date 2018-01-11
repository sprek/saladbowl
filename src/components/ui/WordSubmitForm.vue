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
import { mapState } from 'vuex';

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
  },
};
</script>
<style>
</style>
