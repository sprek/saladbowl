<template>
<v-fade-transition appear>
  <v-container fluid fill-height text-xs-center>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <h1 class="white--text mb-5">Create Game</h1>
        <create-form></create-form>
      </v-flex>
    </v-layout>
  </v-container>
</v-fade-transition>
</template>

<script>
  import CreateForm from '@/components/ui/CreateForm';
  export default {
  name: 'CreateGame',
  components: {
    CreateForm,
  },
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
