<template>
<v-container fluid>
  <v-layout row wrap>
    <v-flex xs12>
      <h2>Round {{round_num}}</h2>
    </v-flex>
    <v-flex xs6 text-xs-right >
      <v-btn color="red" fab dark class="mr-4">
        <v-icon>clear</v-icon>
      </v-btn>
    </v-flex>
    <v-flex xs6 text-xs-left>
      <v-btn color="green" fab dark class="ml-4">
        <v-icon>done</v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

export default {
  name: 'game-display',
  data() {
    return {
      // items: ["test", "blah", "huh"],
    };
  },
  computed: {
    ...mapState(['username', 'players', 'ordered_players', 'game', 'round_num']),
  },
  methods: {
  },
};
</script>

<style>
</style>
