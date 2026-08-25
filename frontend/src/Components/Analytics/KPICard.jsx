import { Card, CardContent, Typography, Box } from "@mui/material";

const KPICard = ({ title, value, subtitle, icon }) => {
  return (
    <Card elevation={2}>
      <CardContent>
        <Box display="flex" justifyContent="space-between">
          <Box>
            <Typography color="text.secondary" variant="body2">
              {title}
            </Typography>

            <Typography variant="h4" fontWeight={700} mt={1}>
              {value}
            </Typography>

            <Typography variant="caption" color="text.secondary">
              {subtitle}
            </Typography>
          </Box>

          {icon}
        </Box>
      </CardContent>
    </Card>
  );
};

export default KPICard;