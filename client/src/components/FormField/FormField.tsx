import { formFieldProps } from "../../global"
import './FormField.css'

const FormField: React.FC<formFieldProps> = ({
    type,
    id,
    name,
    label,
    placeholder,
    register,
    error,
  }) => (
    <>
      <label htmlFor={id}>
        {label}
        {register ? (
            <input className='form-input'
            type={type}
            placeholder={placeholder}
            {...register(name)} />
        ) : (
            <input className='form-input'
        type={type}
        placeholder={placeholder} />
        )}
       
        {error && <p className="error-message">{error.message}</p>}
      </label>
    </>
  );
  export default FormField;