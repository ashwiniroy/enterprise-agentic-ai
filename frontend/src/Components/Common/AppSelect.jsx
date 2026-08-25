import {
    FormControl,
    InputLabel,
    Select,
    MenuItem,
  } from "@mui/material";
  
  const AppSelect = ({
    label,
    value,
    onChange,
    options = [],
    fullWidth = true,
  }) => {
    return (
      <FormControl fullWidth={fullWidth}>
        <InputLabel>{label}</InputLabel>
  
        <Select
          label={label}
          value={value}
          onChange={onChange}
        >
          {options.map((option) => (
            <MenuItem
              key={option.value}
              value={option.value}
            >
              {option.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    );
  };
  
  export default AppSelect;