import { Box, CircularProgress } from "@mui/material";

const Loader = () => {

    return (

        <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            height="300px"
        >

            <CircularProgress />

        </Box>

    );

};

export default Loader;