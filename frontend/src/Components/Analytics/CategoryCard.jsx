import { Card, CardContent, Typography } from "@mui/material";

const CategoryCard = ({ category, count }) => {
  return (
    <Card elevation={2}>
      <CardContent>
        <Typography variant="h6">
          {category}
        </Typography>

        <Typography
          variant="h4"
          mt={2}
          fontWeight={700}
        >
          {count}
        </Typography>

        <Typography
          color="text.secondary"
        >
          Reviews
        </Typography>
      </CardContent>
    </Card>
  );
};

export default CategoryCard;