import { Link, useNavigate } from "react-router-dom";
import FormField from "../../components/FormField/FormField";
import './Login.css';
import axios from 'axios'
import { useForm, SubmitHandler } from 'react-hook-form';


function Login() {
    const { register,
        handleSubmit,
    } = useForm<any>();

    const navigate = useNavigate()
    const onSubmit: SubmitHandler<any> = (data) => {
        const obj={
            password:data.password,
            email:data.email
        }
        axios.post("https://upbeat-server.onrender.com/api/v1/user/login", obj)
        .then((res) => {
            sessionStorage.setItem('access_token',res.data.tokens.access_token)
            sessionStorage.setItem('refresh_token',res.data.tokens.refresh_token)
            navigate('/home')
        })
        .catch(err => console.log(err))
    }
   
    return (
        <div className="login-container relative">
            <div className="form-container">
                <h1>Log in</h1>
                <form className='login-form' onSubmit={handleSubmit(onSubmit)}>
                    <FormField
                        type='text'
                        label='Email'
                        id='email'
                        placeholder='Email'
                        register={register}
                        name="email" />
                    <FormField
                        type='password'
                        label='Password'
                        id='password'
                        placeholder='Password'
                        register={register}
                        name="password"/>
                    <button className='login-button'>Log In</button>
                </form>
                <p>
                    Not a member?
                    <span className='line'>
                        <Link to="/signup">
                            Sign up here
                        </Link>
                    </span>
                </p>
            </div>
        </div>
    )
}

export default Login