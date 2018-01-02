<template>
<v-fade-transition appear>
  <v-container fluid fill-height text-xs-center>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <h1 class="white--text mb-5">Salad Bowl</h1>
        <v-btn to="/create_game">Create Game</v-btn>
        <v-btn to="/join_game">Join Game</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</v-fade-transition>
</template>

<script>
import { mapMutations} from 'vuex';

export default {
  name: 'Home',
  data() {
    return {
    };
  },
  methods: {
  },
}
</script>
<style>
</style>
