interface SkeletonCardsProps {
  count: number;
}
function SkeletonCards({ count }: SkeletonCardsProps) {
  return (
    <div className="flex gap-4">
      {[...Array(count)].map((_, index) => (
        <li
          key={index}
          className="bg-gray-800 rounded-lg px-3 py-4 animate-pulse min-h-52 h-fit flex flex-col gap-2 items-center"
        >
          <div className="bg-gray-400 w-[100px] aspect-square rounded-md flex items-center justify-center">
            <svg
              className="w-10 h-10 text-gray-300 dark:text-gray-600"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 18"
            >
              <path d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z" />
            </svg>
          </div>
          <div className="bg-gray-400 w-1/2 h-4 rounded-lg"></div>
          <div className="bg-gray-400 w-24 h-4 rounded-lg"></div>
        </li>
      ))}
    </div>
  );
}

export default SkeletonCards;
