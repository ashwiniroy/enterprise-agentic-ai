import { TextField } from "@mui/material";

const AppInput = ({
    label,
    value,
    onChange,
    name,
    placeholder,
    type = "text",
    fullWidth = true,
    required = false,
    multiline = false,
    rows = 1,
    error = false,
    helperText = ""
}) => {

    return (

        <TextField
            label={label}
            value={value}
            onChange={onChange}
            name={name}
            placeholder={placeholder}
            type={type}
            fullWidth={fullWidth}
            required={required}
            multiline={multiline}
            rows={rows}
            error={error}
            helperText={helperText}
            variant="outlined"
        />

    );

};

export default AppInput;