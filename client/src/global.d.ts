import { FieldError, UseFormRegister } from "react-hook-form";
import {ZodType, z} from 'zod';

interface Song {
  id: number;
  link: string;
  image: string;
  alt: string;
  artist: string;
  title: string;
  src: string;
}

export interface MusicData {
  "New Released": Song[];
  "Popular Artists": Song[];
  "Popular Tracks": Song[];
}

export type signupFormData = {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
}

export const signupSchema:ZodType<signupFormData> = z
.object({
  username: z.string().min(3, {message: "Username should have at least 3 characters"}),
  email: z.string().email(),
  password: z.string().min(8, {message: "Password is too short"}),
  confirmPassword: z.string(),
})
.refine((data) => data.password === data.confirmPassword, {
  message: "Passwords do not match",
  path: ["confirmPassword"],
});


export type formFieldProps = {
  type: string;
  id: string;
  name: fieldName;
  label: string;
  placeholder?: string;
  register?: UseFormRegister<signupFormData>;
  error?: FieldError | undefined;
}

export type fieldName =
  | "username"
  | "email"
  | "password"
  | "confirmPassword";