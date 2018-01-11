<template>
<v-fade-transition appear>
  <v-container fluid fill-height text-xs-center>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <h1 class="white--text mb-5">Join Game</h1>
        <join-form></join-form>
      </v-flex>
    </v-layout>
  </v-container>
</v-fade-transition>
</template>

<script>
import JoinForm from '@/components/ui/JoinForm';

export default {
  name: 'JoinGame',
  components: {
    JoinForm,
  },
  data() {
    return {
    };
  },
};
</script>
<style>
</style>
