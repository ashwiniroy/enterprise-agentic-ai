import { Card, CardContent, Typography, Box } from "@mui/material";

const StatCard = ({ title, value, icon }) => {
  return (
    <Card elevation={2}>
      <CardContent>
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
        >
          <Box>
            <Typography
              variant="body2"
              color="text.secondary"
            >
              {title}
            </Typography>

            <Typography
              variant="h4"
              fontWeight={700}
              mt={1}
            >
              {value}
            </Typography>
          </Box>

          {icon}
        </Box>
      </CardContent>
    </Card>
  );
};

export default StatCard;