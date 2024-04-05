import { SubmitHandler, useForm } from 'react-hook-form';
import './Signup.css';
import { Link, useNavigate } from 'react-router-dom';
import FormField from '../../components/FormField/FormField';
import { signupFormData, signupSchema } from '../../global.d';
import { zodResolver } from '@hookform/resolvers/zod';
import axios from "axios"


function Signup() {
    const { register,
        handleSubmit,
        formState: { errors, isSubmitting },
        reset,
    } = useForm<signupFormData>({
        resolver: zodResolver(signupSchema),
        mode: "onBlur",
    });

    const navigate = useNavigate()
    const onSubmit: SubmitHandler<signupFormData> = (data) => {
        const obj = {
            firstname: data.username,
            lastname:data.username,
            username:data.username,
            email:data.email,
            password:data.password
        }
        axios.post("https://upbeat-server.onrender.com/api/v1/user/register", obj)
            .then(res => {
                console.log(res)
                alert("Congratulations! Your account has been created successfully.");
                reset();
                navigate('/login');
            })
            .catch(err => console.log(err))

    };

    return (
        <div className="signup-container relative">
            <div className="form-container">
                <h1>Sign up</h1>
                <form className='signup-form' onSubmit={handleSubmit(onSubmit)}>
                    <FormField
                        type='text'
                        label='Username'
                        id='username'
                        placeholder='Username'
                        name='username'
                        register={register}
                        error={errors.username} />
                    <FormField
                        type='text'
                        label='Email'
                        id='email'
                        placeholder='Email'
                        name='email'
                        register={register}
                        error={errors.email} />
                    <FormField
                        type='password'
                        label='Password'
                        id='password'
                        name='password'
                        register={register}
                        error={errors.password} />
                    <FormField
                        type='password'
                        label='Confirm Password'
                        id='confirmPassword'
                        name='confirmPassword'
                        register={register}
                        error={errors.confirmPassword} />

                    <button className='signup-button' disabled={isSubmitting}>Sign up</button>
                </form>
                <p>
                    Already have an account?
                    <span className='line'>
                        <Link to="/login">
                            Log in
                        </Link>
                    </span>
                </p>
            </div>
        </div>

    )
}

export default Signup