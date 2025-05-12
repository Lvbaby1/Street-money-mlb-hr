# Optional: Format HR probabilities if column exists
if 'hr_probability' in filtered_df.columns:
    filtered_df['hr_probability'] = filtered_df['hr_probability'].apply(lambda x: f"{x:.0%}")
