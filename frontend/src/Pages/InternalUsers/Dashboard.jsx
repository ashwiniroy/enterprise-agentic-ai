import React from "react";
import Grid from "@mui/material/Grid";
import DashboardHeader from "../../Components/Dashboard/DashboardHeader";
import StatCard from "../../Components/Dashboard/StatCard";
import RecentReviewCard from "../../Components/Dashboard/RecentReviewCard";
import { getReviews } from "../../Services/api/ReviewAPI";

import ReviewsIcon from "@mui/icons-material/RateReview";
import ThumbUpIcon from "@mui/icons-material/ThumbUp";
import ThumbDownIcon from "@mui/icons-material/ThumbDown";
import StarIcon from "@mui/icons-material/Star";

const Dashboard = () => {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    getReviews()
      .then((response) => {
        setData(response);
        console.log("Reviews:", response);
      })
      .catch((error) => {
        console.error("Failed to fetch reviews:", error);
      });
  }, []);

  const positiveReviews = data.filter(
    (item) => item.sentiment === "POSITIVE"
  );

  const negativeReviews = data.filter(
    (item) => item.sentiment === "NEGATIVE"
  );

  const neutralReviews = data.filter(
    (item) => item.sentiment === "NEUTRAL"
  );

  const averageRating =
    data.length > 0
      ? (
          data.reduce(
            (total, review) => total + Number(review.rating || 0),
            0
          ) / data.length
        ).toFixed(1)
      : "0.0";

      const latestReviews = data.slice(-3).reverse();
  return (
    <>
      <DashboardHeader />

      <Grid container spacing={3} mb={4}>
        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Total Reviews"
            value={data.length}
            icon={<ReviewsIcon color="primary" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Positive"
            value={positiveReviews.length}
            icon={<ThumbUpIcon color="success" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Negative"
            value={negativeReviews.length}
            icon={<ThumbDownIcon color="error" />}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <StatCard
            title="Average Rating"
            value={averageRating}
            icon={<StarIcon color="warning" />}
          />
        </Grid>
      </Grid>

      <DashboardHeader />

      {
        latestReviews.map((review) => (
          <RecentReviewCard
            key={review.id}
            customer={review.customerName}
            title={review.reviewTitle}
            rating={review.rating}
            sentiment={review.sentiment}
          />
        ))
      }
    </>
  );
};

export default Dashboard;