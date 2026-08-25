import {
    Box,
    Grid,
    Typography
  } from "@mui/material";
  
  import ReviewsIcon from "@mui/icons-material/RateReview";
  import ThumbUpIcon from "@mui/icons-material/ThumbUp";
  import ThumbDownIcon from "@mui/icons-material/ThumbDown";
  import StarIcon from "@mui/icons-material/Star";
  
  import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Tooltip,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    LineChart,
    Line
  } from "recharts";
  
  import KPICard from "../../Components/Analytics/KPICard";
  import ChartContainer from "../../Components/Analytics/ChartContainer";
  import CategoryCard from "../../Components/Analytics/CategoryCard";
  
  const sentimentData = [
    { name: "Positive", value: 980 },
    { name: "Neutral", value: 120 },
    { name: "Negative", value: 150 },
  ];
  
  const ratingData = [
    { rating: "1", reviews: 20 },
    { rating: "2", reviews: 50 },
    { rating: "3", reviews: 150 },
    { rating: "4", reviews: 400 },
    { rating: "5", reviews: 630 },
  ];
  
  const monthlyData = [
    { month: "Jan", reviews: 120 },
    { month: "Feb", reviews: 180 },
    { month: "Mar", reviews: 240 },
    { month: "Apr", reviews: 260 },
    { month: "May", reviews: 300 },
    { month: "Jun", reviews: 350 },
  ];
  
  const COLORS = [
    "#4CAF50",
    "#FFC107",
    "#F44336",
  ];
  
  const Analytics = () => {
    return (
      <Box>
  
        <Typography
          variant="h4"
          fontWeight={700}
          mb={4}
        >
          Analytics
        </Typography>
  
        {/* KPI Cards */}
  
        <Grid container spacing={3} mb={4}>
  
          <Grid size={{ xs:12, md:3 }}>
            <KPICard
              title="Total Reviews"
              value="1,250"
              subtitle="+12% this month"
              icon={<ReviewsIcon color="primary" />}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <KPICard
              title="Positive Reviews"
              value="980"
              subtitle="78%"
              icon={<ThumbUpIcon color="success" />}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <KPICard
              title="Negative Reviews"
              value="150"
              subtitle="12%"
              icon={<ThumbDownIcon color="error" />}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <KPICard
              title="Average Rating"
              value="4.6"
              subtitle="Excellent"
              icon={<StarIcon color="warning" />}
            />
          </Grid>
  
        </Grid>
  
        {/* Charts */}
  
        <Grid container spacing={3}>
  
          <Grid size={{ xs:12, md:6 }}>
            <ChartContainer title="Rating Distribution">
  
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={ratingData}>
                  <CartesianGrid strokeDasharray="3 3"/>
                  <XAxis dataKey="rating"/>
                  <YAxis/>
                  <Tooltip/>
                  <Bar dataKey="reviews" fill="#1976d2"/>
                </BarChart>
              </ResponsiveContainer>
  
            </ChartContainer>
          </Grid>
  
          <Grid size={{ xs:12, md:6 }}>
            <ChartContainer title="Sentiment Distribution">
  
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={sentimentData}
                    dataKey="value"
                    outerRadius={100}
                  >
                    {
                      sentimentData.map((entry,index)=>(
                        <Cell
                          key={index}
                          fill={COLORS[index]}
                        />
                      ))
                    }
                  </Pie>
                  <Tooltip/>
                </PieChart>
              </ResponsiveContainer>
  
            </ChartContainer>
          </Grid>
  
          <Grid size={{ xs:12 }}>
            <ChartContainer title="Monthly Review Trend">
  
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={monthlyData}>
                  <CartesianGrid strokeDasharray="3 3"/>
                  <XAxis dataKey="month"/>
                  <YAxis/>
                  <Tooltip/>
                  <Line
                    type="monotone"
                    dataKey="reviews"
                    stroke="#1976d2"
                    strokeWidth={3}
                  />
                </LineChart>
              </ResponsiveContainer>
  
            </ChartContainer>
          </Grid>
  
        </Grid>
  
        {/* Categories */}
  
        <Typography
          variant="h5"
          mt={5}
          mb={3}
        >
          Top Categories
        </Typography>
  
        <Grid container spacing={3}>
  
          <Grid size={{ xs:12, md:3 }}>
            <CategoryCard
              category="Laptop"
              count={420}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <CategoryCard
              category="Mobile"
              count={380}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <CategoryCard
              category="Accessories"
              count={250}
            />
          </Grid>
  
          <Grid size={{ xs:12, md:3 }}>
            <CategoryCard
              category="Tablet"
              count={200}
            />
          </Grid>
  
        </Grid>
  
      </Box>
    );
  };
  
  export default Analytics;