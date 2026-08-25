import { Card, CardContent, Typography } from "@mui/material";

const ChartContainer = ({ title, children }) => {
  return (
    <Card elevation={2}>
      <CardContent>
        <Typography
          variant="h6"
          mb={3}
          fontWeight={600}
        >
          {title}
        </Typography>

        {children}
      </CardContent>
    </Card>
  );
};

export default ChartContainer;