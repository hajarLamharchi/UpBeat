import { Slider } from "@mantine/core";
import { useHover } from "@mantine/hooks";

interface SliderHoverProps {
  barStyles?: React.CSSProperties;
  thumbStyles?: React.CSSProperties;
  trackStyles?: React.CSSProperties;
  trackRef: React.RefObject<any>;
  value?: any;
  setCurrentTime?: (time: number) => void;
  size: number;
  onVolumeChange?: (value: number) => void;
}

export function SliderHover({
  barStyles,
  thumbStyles,
  trackStyles,
  trackRef,
  value,
  setCurrentTime,
  size,
  onVolumeChange,
}: SliderHoverProps) {
  const { hovered, ref } = useHover();

  return (
    <Slider
      min={0}
      max={100}
      defaultValue={50}
      ref={ref}
      label={null}
      styles={{
        thumb: {
          transition: "opacity 150ms ease",
          opacity: hovered ? 1 : 0,
          ...thumbStyles,
        },
        bar: barStyles,
        root: trackStyles,
      }}
      size={size}
      value={value}
      onChange={(value) => {
        if (onVolumeChange) {
          onVolumeChange(value / 100);
        } else if (setCurrentTime) {
          if (trackRef.current) {
            const time = (trackRef.current.duration / 100) * value;
            trackRef.current.currentTime = time;
            setCurrentTime(time);
          }
        }
      }}
    />
  );
}
