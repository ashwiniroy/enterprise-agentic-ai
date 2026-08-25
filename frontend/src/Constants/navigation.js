import DashboardIcon from "@mui/icons-material/Dashboard";
import RateReviewIcon from "@mui/icons-material/RateReview";
import AddCommentIcon from "@mui/icons-material/AddComment";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import SettingsIcon from "@mui/icons-material/Settings";

export const navigationItems = [
  {
    title: "Dashboard",
    path: "/dashboard",
    icon: <DashboardIcon />,
  },
  {
    title: "Reviews",
    path: "/reviews",
    icon: <RateReviewIcon />,
  },
  {
    title: "Create Review",
    path: "/create-review",
    icon: <AddCommentIcon />,
  },
  {
    title: "Analytics",
    path: "/analytics",
    icon: <AnalyticsIcon />,
  },
  {
    title: "AI Search",
    path: "/ai-search",
    icon: <SmartToyIcon />,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: <SettingsIcon />,
  },
];