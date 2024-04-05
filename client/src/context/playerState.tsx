import React, { useReducer } from "react";
import playerReducer from "./playerReducer";
import playerContext from "./playerContext";
import { Song } from "../global.d";

interface PlayerStateProps {
  children: React.ReactNode;
}

const PlayerState = ({ children }: PlayerStateProps) => {
  const initialState = {
    playlist: [],
    currentSong: null,
    isPlaying: false,
    song: null,
    repeat: false,
    isShuffle: false,
    isRepeat: false,
    isRepeatOnce: false,
    isLoggedin: false,
  };

  const [state, dispatch] = useReducer(playerReducer, initialState);

  const setIsLoggedin = (value: boolean) => {
    dispatch({ type: "SET_IS_LOGGEDIN", payload: value });
  };

  const setCurrentSong = (id: number) => {
    dispatch({ type: "SET_Current_Song", payload: id });
  };

  const setPlaylist = (playlist: [Song]) => {
    dispatch({ type: "SET_PLAYLIST", payload: playlist });
  };

  const likeSong = (id: number) => {
    dispatch({ type: "Like", payload: id });
  };

  const setNextSong = () => {
    let index = state.currentSong;
    if (state.isShuffle) {
      index = Math.floor(Math.random() * state.playlist.length - 1);
      while (state.currentSong === index) {
        index = Math.floor(Math.random() * state.playlist.length - 1);
      }
    } else {
      index = index + 1;
    }
    dispatch({ type: "SET_Current_Song", payload: index });
  };

  const setPrevSong = () => {
    let index = state.currentSong;
    if (state.isShuffle) {
      index = Math.floor(Math.random() * state.playlist.length);
    } else {
      index = (index - 1 + state.playlist.length) % state.playlist.length;
    }
    dispatch({ type: "SET_Current_Song", payload: index });
  };

  const toggleShuffle = () => {
    dispatch({ type: "SET_SHUFFLE", payload: !state.isShuffle });
  };

  const toggleRepeat = () => {
    if (state.isRepeatOnce) {
      dispatch({ type: "SET_REPEAT", payload: !state.isRepeat });
      dispatch({ type: "SET_REPEAT_ONCE", payload: !state.isRepeatOnce });
    } else if (state.isRepeat) {
      dispatch({ type: "SET_REPEAT", payload: !state.isRepeat });
    } else {
      dispatch({ type: "SET_REPEAT_ONCE", payload: !state.isRepeatOnce });
    }
  };

  const togglePlay = () => {
    if (state.isPlaying) {
      dispatch({ type: "PAUSE", payload: !state.isPlaying });
    } else {
      dispatch({ type: "PLAY", payload: !state.isPlaying });
    }
  };

  const toggleRepeatOnce = () => {
    dispatch({ type: "SET_REPEAT_ONCE", payload: !state.isRepeatOnce });
  };

  return (
    <playerContext.Provider
      value={{
        playlist: state.playlist,
        currentSong: state.currentSong,
        isPlaying: state.isPlaying,
        song: state.song,
        isShuffle: state.isShuffle,
        isRepeat: state.isRepeat,
        isRepeatOnce: state.isRepeatOnce,
        setCurrentSong,
        setPlaylist,
        likeSong,
        setNextSong,
        setPrevSong,
        toggleShuffle,
        togglePlay,
        toggleRepeat,
        toggleRepeatOnce,
        isLoggedin: state.isLoggedin,
        setIsLoggedin,
      }}
    >
      {children}
    </playerContext.Provider>
  );
};

export default PlayerState;
