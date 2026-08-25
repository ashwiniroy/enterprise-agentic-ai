import SearchIcon from "@mui/icons-material/Search";
import { InputAdornment, TextField } from "@mui/material";

const SearchBar = ({
    value,
    onChange,
    placeholder = "Search..."
}) => {

    return (

        <TextField
            fullWidth
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            InputProps={{
                startAdornment: (
                    <InputAdornment position="start">

                        <SearchIcon />

                    </InputAdornment>
                )
            }}
        />

    );

};

export default SearchBar;