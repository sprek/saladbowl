<template>
<v-container fluid text-xs-center>
  <v-layout row wrap align-center>
    <v-flex xs12 md6 offset-md3>
      <v-card>
        <v-container fluid>
        <v-layout row wrap>
        <v-flex xs12>
          <p>{{ room_id }}</p>
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
    if (!this.room_id) this.set_room_id(this.$route.params.room_id);
    const params = {
      room_id: this.room_id,
    };
    this.$socket.emit('join', params);
  },
  computed: {
    ...mapState(['connected','room_id','error'])
  },
  methods: {
    ...mapMutations(['set_room_id'])
  },
};
</script>

<style>
</style>
