import { Box, Typography } from "@mui/material";

const PageHeader = ({ title, subtitle, action }) => {

    return (

        <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            mb={4}
        >

            <Box>

                <Typography variant="h4">

                    {title}

                </Typography>

                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    {subtitle}
                </Typography>

            </Box>

            {action}

        </Box>

    );

};

export default PageHeader;