<template>
<v-card>
  <v-card-text>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12>
          <v-form v-model="valid">
            <v-text-field v-model="reqUsername" label="Username" required :rules="[v => !!v || 'Item is required']"></v-text-field>
            <v-text-field v-model="reqRoomId" label="Room ID" mask="AAAA" required :rules="[v => !!v || 'Item is required']"></v-text-field>
          </v-form>
        </v-flex>
        <v-flex xs12>
          <v-btn block class="mt-3" @click.stop="joinGame">Join Game</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card-text>
</v-card>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'join-form',
  data() {
    return {
      reqUsername: '',
      reqRoomId: '',
      valid: false,
    };
  },
  computed: {
    ...mapState(['room_id', 'username']),
  },
  watch: {
    room_id() {
      console.log(`SETTING ROOM ID: ${this.room_id}`);
      // this.set_room_id(this.room_id);
      this.$router.push({ name: 'Game', params: { room_id: this.room_id }, query: {user: this.reqUsername}});
    },
  },
  methods: {
    ...mapMutations(['set_username']),
    joinGame() {
      if (!this.valid) return;
      this.set_username(this.reqUsername);
      const params = {
        username: this.reqUsername,
        room_id: this.reqRoomId,
      };
      console.log(`JOINING ROOM: ${params.room_id}`);
      this.$socket.emit('join', params);
    },
  },
};
</script>

<style>
</style>
