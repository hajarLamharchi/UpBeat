import "./TrackContrainer.css";
import NewReleasedItems from "../NewReleasedItems/NewReleasedItems";
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io";
import { useState } from "react";

function TrackContainer() {
  const [clickedRight, setClickedRight] = useState(0);
  const [clickedLeft, setClickedLeft] = useState(0);
  const click_right = () => {
    setClickedRight((last_value) => last_value + 1);
  };
  const click_left = () => {
    setClickedLeft((last_value) => last_value + 1);
  };

  return (
    <div className="track-container home-sections">
      <div className="container-header">
        <h2>New Released</h2>
        <div className="navigate-container">
          <button onClick={() => click_left()} className="navigate-button">
            <IoIosArrowBack />
          </button>
          <button onClick={() => click_right()} className="navigate-button">
            <IoIosArrowForward />
          </button>
        </div>
      </div>
      <NewReleasedItems clickedLeft={clickedLeft} clickedRight={clickedRight} />
    </div>
  );
}

export default TrackContainer;
