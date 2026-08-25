import { Box, Typography } from "@mui/material";

const DashboardHeader = () => {
  return (
    <Box mb={4}>
      <Typography variant="h4" fontWeight={700}>
        Dashboard
      </Typography>

      <Typography
        variant="body1"
        color="text.secondary"
        mt={1}
      >
        Welcome back 👋
      </Typography>
    </Box>
  );
};

export default DashboardHeader;