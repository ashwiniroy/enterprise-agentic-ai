import { useState } from "react";

import {
  Box,
  Grid,
  Paper,
  Typography,
  RadioGroup,
  Radio,
  FormControlLabel,
  Rating,
} from "@mui/material";

import AppInput from "../../Components/Common/Input";
import AppButton from "../../Components/Common/Button";
import AppSelect from "../../Components/Common/AppSelect";
import { createReview } from "../../Services/api/ReviewAPI";
import { PRODUCTS } from "../../Constants/products";
import { CATEGORIES } from "../../Constants/categories";




const ReviewForm = () => {
  const [formData, setFormData] = useState({
    customerName: "",
    email: "",
    product: "",
    category: "",
    purchaseDate: "",
    rating: 0,
    reviewTitle: "",
    reviewDescription: "",
    recommend: "yes",
  });

  const handleChange = (field, value) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  const handleReset = () => {
    setFormData({
      customerName: "",
      email: "",
      product: "",
      category: "",
      purchaseDate: "",
      rating: 0,
      reviewTitle: "",
      reviewDescription: "",
      recommend: "yes",
    });
  };

  const handleSubmit = async () => {
    try {
      const payload = {
        ...formData,
        recommend: formData.recommend === "yes",
      };
  
      const response = await createReview(payload);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Box>

      <Typography
        variant="h4"
        fontWeight={700}
        mb={4}
      >
        Create Review
      </Typography>

      {/* Customer Information */}

      <Paper elevation={2} sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" mb={3}>
          Customer Information
        </Typography>

        <Grid container spacing={3}>
          <Grid size={{ xs: 12, md: 6 }}>
            <AppInput
              label="Customer Name"
              value={formData.customerName}
              onChange={(e) =>
                handleChange("customerName", e.target.value)
              }
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <AppInput
              label="Email Address"
              type="email"
              value={formData.email}
              onChange={(e) =>
                handleChange("email", e.target.value)
              }
            />
          </Grid>
        </Grid>
      </Paper>

      {/* Product Information */}

      <Paper elevation={2} sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" mb={3}>
          Product Information
        </Typography>

        <Grid container spacing={3}>
          <Grid size={{ xs: 12, md: 6 }}>
            <AppSelect
              label="Product"
              value={formData.product}
              onChange={(e) =>
                handleChange("product", e.target.value)
              }
              options={PRODUCTS}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <AppSelect
              label="Category"
              value={formData.category}
              onChange={(e) =>
                handleChange("category", e.target.value)
              }
              options={CATEGORIES}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <AppInput
              label="Purchase Date"
              type="date"
              value={formData.purchaseDate}
              onChange={(e) =>
                handleChange("purchaseDate", e.target.value)
              }
            />
          </Grid>
        </Grid>
      </Paper>

      {/* Review Details */}

      <Paper elevation={2} sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" mb={3}>
          Review Details
        </Typography>

        <Grid container spacing={3}>
          <Grid size={{ xs: 12 }}>
            <Typography gutterBottom>
              Overall Rating
            </Typography>

            <Rating
              size="large"
              value={formData.rating}
              onChange={(event, value) =>
                handleChange("rating", value)
              }
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <AppInput
              label="Review Title"
              value={formData.reviewTitle}
              onChange={(e) =>
                handleChange("reviewTitle", e.target.value)
              }
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <AppInput
              label="Review Description"
              multiline
              rows={5}
              value={formData.reviewDescription}
              onChange={(e) =>
                handleChange("reviewDescription", e.target.value)
              }
            />
          </Grid>
        </Grid>
      </Paper>

      {/* Recommendation */}

      <Paper elevation={2} sx={{ p: 3 }}>
        <Typography variant="h6" mb={2}>
          Would you recommend this product?
        </Typography>

        <RadioGroup
          row
          value={formData.recommend}
          onChange={(e) =>
            handleChange("recommend", e.target.value)
          }
        >
          <FormControlLabel
            value="yes"
            control={<Radio />}
            label="Yes"
          />

          <FormControlLabel
            value="no"
            control={<Radio />}
            label="No"
          />
        </RadioGroup>
      </Paper>

      {/* Buttons */}

      <Box
        mt={4}
        display="flex"
        justifyContent="flex-end"
        gap={2}
      >
        <AppButton
          variant="outlined"
          onClick={handleReset}
        >
          Reset
        </AppButton>

        <AppButton
          onClick={handleSubmit}
        >
          Submit Review
        </AppButton>
      </Box>

    </Box>
  );
};

export default ReviewForm;