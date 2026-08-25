import { Card, CardContent, Typography, Rating } from "@mui/material";

const SourceReviewCard = ({ customer, rating, review }) => {
  return (
    <Card sx={{ mb: 2 }}>
      <CardContent>
        <Typography fontWeight={600}>
          {customer}
        </Typography>

        <Rating value={rating} readOnly size="small" />

        <Typography mt={1} color="text.secondary">
          {review}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default SourceReviewCard;