import { useEffect, useRef } from "react";
import wavyBackground from "../../public/assets/wavy-background.mp4";

export const WavyBackground = () => {
  const ref = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (ref.current) {
      console.log(ref.current);
      ref.current.disablePictureInPicture = true;
    }
  }, [ref]);

  return (
    <video
      ref={ref}
      controlsList="nodownload"
      disablePictureInPicture
      autoPlay
      loop
      muted
      className="w-full h-full object-cover absolute top-0 left-0"
    >
      <source src={wavyBackground} type="video/mp4" />
    </video>
  );
};
