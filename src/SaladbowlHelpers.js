const SB_CONSTS = {
  'GS_WAITING_FOR_WORDS':'WAITING_FOR_WORDS',
  'GS_WAITING_TO_START':'WAITING_TO_START',
  'GS_WAITING_ON_TURN':'WAITING_ON_TURN',
  'GS_PLAYING':'PLAYING',
  'GS_ROUND1':'ROUND1',
  'GS_ROUND2':'ROUND2',
  'GS_ROUND3':'ROUND3',
  'GS_ROUND4':'ROUND4',
  'GS_FINISHED':'FINISHED',
};

export default {
  install: (Vue) => {
    Vue.prototype.$sb_helpers = {
      getConst(key) {
        return SB_CONSTS[key];
      }
    };
  },
};
