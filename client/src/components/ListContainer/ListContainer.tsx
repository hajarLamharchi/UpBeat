import { useState } from "react";
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io";
import { Link } from "react-router-dom";

interface ListContainerProps {
  title: string;
  isScrollable?: boolean;
  id?: string;
  children: React.ReactNode;
}

function ListContainer({
  title,
  isScrollable = false,
  id,
  children,
}: ListContainerProps) {
  const [clickedRight, setClickedRight] = useState(0);
  const [clickedLeft, setClickedLeft] = useState(0);
  const click_right = () => {
    setClickedRight((last_value) => last_value + 1);
  };
  const click_left = () => {
    setClickedLeft((last_value) => last_value + 1);
  };

  return (
    <div>
      <header className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-shadow">{title}</h2>
        <div className="flex gap-3 justify-center items-center">
          {isScrollable && (
            <div className="navigate-container">
              <button onClick={() => click_left()} className="navigate-button">
                <IoIosArrowBack />
              </button>
              <button onClick={() => click_right()} className="navigate-button">
                <IoIosArrowForward />
              </button>
            </div>
          )}
          <Link
            to={`/playlist/${id}`}
            className="border border-gray-400 px-3 rounded-full cursor-pointer hover:bg-gray-700 transition-colors duration-150 ease-in-out group"
          >
            <span className="text-sm text-gray-400 group-hover:text-white">
              See all
            </span>
          </Link>
        </div>
      </header>
      {children}
    </div>
  );
}

export default ListContainer;
