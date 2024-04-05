interface IState {
  playlist: any[];
  currentSong: any;
  isPlaying: boolean;
  song: any;
  isShuffle: boolean;
  isRepeat: boolean;
  isRepeatOnce: boolean;
  isLoggedin: boolean;
}

interface IAction {
  type: string;
  payload: any;
}

let playerReducer = (state: IState, action: IAction) => {
  switch (action.type) {
    case "SET_PLAYLIST":
      return {
        ...state,
        playlist: action.payload,
      };
    case "SET_Current_Song":
      return {
        ...state,
        currentSong: action.payload,
        isPlaying: true,
      };
    case "PLAY":
      return {
        ...state,
        isPlaying: true,
      };
    case "PAUSE":
      return {
        ...state,
        isPlaying: false,
      };
    case "SET_SONG":
      return {
        ...state,
        song: action.payload,
      };
    case "SET_REPEAT":
      return {
        ...state,
        isRepeat: action.payload,
      };
    case "SET_REPEAT_ONCE":
      return {
        ...state,
        isRepeatOnce: action.payload,
      };
    case "SET_SHUFFLE":
      return {
        ...state,
        isShuffle: action.payload,
      };
    case "Like":
      return {
        ...state,
        playlist: state.playlist.map((song) => {
          if (song.id === action.payload) {
            return { ...song, isLiked: !song.isLiked };
          }
          return song;
        }),
      };
    case "SET_IS_LOGGEDIN":
      return {
        ...state,
        isLoggedin: action.payload,
      };
    default:
      return state;
  }
};

export default playerReducer;
