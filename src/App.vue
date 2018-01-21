<template>
<v-app dark>
  <v-navigation-drawer temporary v-model="drawer" fixed>
    <v-list>
      <v-divider></v-divider>
      <v-list-tile v-for="item in items" :key="item.title" :to="{ name: item.route }">
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar fixed app>
    <v-btn icon @click.stop="drawer = !drawer"  class="hidden-sm-and-up">
      <v-icon>menu</v-icon>
    </v-btn>
    <v-toolbar-title>{{ dynamic_title }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-xs-only">
      <template v-for="item in toolbar_items">
        <v-btn  :key="item.title" :to="{ name: item.route }" active-class="">
          <v-icon left dark>{{ item.icon }}</v-icon>{{ item.title }}
        </v-btn>
      </template>
    </v-toolbar-items>
    
  </v-toolbar>
  <v-content>
    <router-view></router-view>
  </v-content>
  <v-alert color="error" icon="warning" value="true" v-if="error" fixed>
    {{error}}
  </v-alert>
</v-app>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'app',
  data() {
    return {
      drawer: false,
      title: 'Salad Bowl',
      items: [
        { title: 'Home', icon: 'home', route: 'Home' },
        { title: 'Word List', icon: 'list', route: 'WordList' },
      ],
      toolbar_items: [
        { title: 'Word List', icon: 'list', route: 'WordList' },
        { title: 'Home', icon: 'home', route: 'Home' },
      ],
    };
  },
  computed: {
    ...mapState(['connected', 'room', 'error']),
    dynamic_title: function () {
      if (this.$route.path === '/') {
        return 'Salad Bowl';
      } else if (this.$route.path === '/word_list') {
        return 'Word List';
      } else if (this.$route.path === '/create_game') {
        return 'Salad Bowl';
      } else if (this.$route.path === '/join_game') {
        return 'Salad Bowl';
      } else if (this.$route.path.substring(0, 5) === '/game') {
        return `Game: ${this.$route.path.substring(6)}`;
      }
      return this.$route.path;
    },
  },
};
</script>
