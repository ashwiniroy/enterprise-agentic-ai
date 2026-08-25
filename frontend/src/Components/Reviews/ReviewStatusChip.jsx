import Chip from "@mui/material/Chip";

const ReviewStatusChip = ({ status }) => {
  return (
    <Chip
      label={status}
      color={status === "Active" ? "success" : "default"}
      size="small"
      variant="filled"
    />
  );
};

export default ReviewStatusChip;