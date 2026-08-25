import { Box, Typography } from "@mui/material";
import InboxIcon from "@mui/icons-material/Inbox";

const EmptyState = ({ message = "No Data Found" }) => {

    return (

        <Box
            textAlign="center"
            py={8}
        >

            <InboxIcon
                sx={{
                    fontSize: 70,
                    color: "#94A3B8"
                }}
            />

            <Typography mt={2}>

                {message}

            </Typography>

        </Box>

    );

};

export default EmptyState;