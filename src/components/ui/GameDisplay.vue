<template>
<v-container fluid>
  <v-layout row wrap>
    <v-flex xs12>
    <h2>Round {{round_num}}</h2>
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
