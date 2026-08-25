import {
    Card,
    CardContent,
    Typography,
    Chip,
    Rating,
    Stack,
  } from "@mui/material";
  
  const RecentReviewCard = ({
    customer,
    title,
    rating,
    sentiment,
  }) => {
    return (
      <Card sx={{ mb: 2 }}>
        <CardContent>
          <Typography fontWeight={600}>
            {customer}
          </Typography>
  
          <Typography
            variant="body2"
            color="text.secondary"
            mt={1}
          >
            {title}
          </Typography>
  
          <Stack
            direction="row"
            spacing={2}
            mt={2}
            alignItems="center"
          >
            <Rating
              value={rating}
              readOnly
              size="small"
            />
  
            <Chip
              label={sentiment}
              color={
                sentiment === "Positive"
                  ? "success"
                  : sentiment === "Negative"
                  ? "error"
                  : "warning"
              }
              size="small"
            />
          </Stack>
        </CardContent>
      </Card>
    );
  };
  
  export default RecentReviewCard;