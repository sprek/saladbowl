<template>
<v-container fluid text-xs-center>
  <v-layout row wrap align-center>
    <v-flex xs12>
      <v-card mt-0 ml-0 mr-0>
        <v-container fluid>
        <v-layout row wrap text-xs-left>
          <v-flex xs12>
            <subheading>Logged in as: {{ username }}</subheading>
          </v-flex>
        </v-layout row wrap>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import { mapState, mapMutations} from 'vuex';

export default {
  name: 'game-board',
  data() {
    return {
    }
  },
  mounted() {
    //if (!this.username) this.set_username('unknown');
    //const params = {
    //  username: this.username,
    //  room_id: this.room_id,
    //};
    if (!this.room_id) {
      this.$router.push({name: 'JoinGame', params: {reqRoomId: this.$route.params.room_id } });
    }
  },
  computed: {
    ...mapState(['connected','room_id','username', 'error'])
  },
  methods: {
    ...mapMutations(['set_room_id', 'set_username'])
  },
};
</script>

<style>
</style>
