import React from 'react';
import {AbsoluteFill, Audio, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

export type LessonScene = {
  title: string;
  narration: string;
  body: string;
  accent?: string;
  audioSrc?: string;
};

export const ArabicLessonFrame: React.FC<{scene: LessonScene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const opacity = interpolate(frame, [0, 12, durationInFrames - 12, durationInFrames], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <AbsoluteFill dir="rtl" style={{fontFamily: 'Noto Naskh Arabic, sans-serif', background: '#08111f', color: '#f8fafc', padding: 72, textAlign: 'right'}}>
    <div style={{opacity, direction: 'rtl', unicodeBidi: 'plaintext', maxWidth: 1050, margin: 'auto'}}>
      <div style={{width: 96, height: 10, background: scene.accent ?? '#4fd1c5', marginBottom: 38}} />
      <h1 style={{fontSize: 64, lineHeight: 1.25, margin: 0}}>{scene.title}</h1>
      <p style={{fontSize: 38, lineHeight: 1.55, marginTop: 44}}>{scene.body}</p>
    </div>
    {scene.audioSrc ? <Audio src={scene.audioSrc} /> : null}
  </AbsoluteFill>;
};
