<template>
<v-card>
  <v-card-text>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <v-form v-model="valid">
            <v-text-field v-model="reqUsername" label="User Name" required :rules="[v => !!v || 'Item is required']"></v-text-field>
            <v-select v-bind:items="numWordsOptions" v-model="numWordsPerPlayer"
                      label="Number of words per player"></v-select>
          </v-form>
        </v-flex>
        <v-flex xs12>
          <v-btn block class="mt-3" @click.stop="createGame">Start Game</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card-text>
</v-card>
</template>

<script>
import { mapState, mapMutations} from 'vuex';
export default {
  name: 'create-form',
  data() {
    return {
      reqUsername: '',
      numWordsPerPlayer: 3,
      numWordsOptions: [1,2,3,4,5],
      valid: false,
    };
  },
  computed: {
    ...mapState(['room_id', 'username', 'game']),
  },
  watch: {
    game() {
      console.log ("REQ USERNAME IS: " + this.reqUsername);
      console.log ("SETTING ROOM ID: " + this.room_id);
      this.set_username(this.reqUsername);
      this.$router.push({name: 'Game', params: {room_id: this.room_id } });
    },
  },
  methods: {
    ...mapMutations(['set_username']),
    createGame() {
      if (!this.valid) return;
      console.log ("CREATING GAME WITH: " + this.reqUsername + ", " + this.numWordsPerPlayer);
      const params = {
        username: this.reqUsername,
        numWordsPerPlayer: this.numWordsPerPlayer,
      };
      this.$socket.emit('create', params);
    }
  }
}
</script>
<style>
</style>
