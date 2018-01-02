import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/views/Home';
import Game from '@/components/views/Game';
import CreateGame from '@/components/views/CreateGame';
import JoinGame from '@/components/views/JoinGame';
import WordList from '@/components/views/WordList';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/create_game',
      name: 'CreateGame',
      component: CreateGame,
    },
    {
      path: '/join_game',
      name: 'JoinGame',
      component: JoinGame,
    },
    {
      path: '/game/:room_id',
      name: 'Game',
      component: Game,
    },
    {
      path: '/word_list',
      name: 'WordList',
      component: WordList,
    },
  ],
});
