<template>
<v-container fluid text-xs-center>
  <v-layout row wrap align-center>
    <v-flex xs12>
      <v-card>
        <v-container fluid>
          <v-layout row wrap>
            <v-flex xs6 text-xs-left>
              <h4>Logged in as: {{ username }}</h4>
            </v-flex>
            <v-flex xs6 text-xs-right>
              <h4># Players: {{players.length}}</h4>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
      <v-card>
        <v-container fluid>
          <v-layout row wrap text-xs-left>
            <v-flex xs12>
              <h1 class="white--text">Submit Words / Phrases</h1>
              <word-submit-form></word-submit-form>
            </v-flex>
          </v-layout row wrap>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import WordSubmitForm from '@/components/ui/WordSubmitForm';
import { mapState } from 'vuex';

export default {
  name: 'game-board',
  components: {
    WordSubmitForm,
  },
  data() {
    return {
    };
  },
  // watch: {
  //   game() {
  //     console.log ("GOT GAME UPDATE");
  //     this.numPlayers = this.game.players.length;
  //   },
  //   numtest() {
  //     console.log ("GOT NUMTEST UPDATE");
  //   },
  // },
  mounted() {
    if (!this.room_id) {
      this.$router.push({ name: 'JoinGame', params: { reqRoomId: this.$route.params.room_id } });
    }
  },
  computed: {
    ...mapState(['connected', 'room_id', 'error', 'players', 'username', 'game', 'numtest']),
  },
  methods: {
  },
};
</script>

<style>
</style>
