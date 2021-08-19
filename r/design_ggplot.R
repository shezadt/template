# Design of my ggplot charts

# Theme for all plots
theme_visual <- theme_classic() +
  theme(plot.title.position = "plot",
        plot.caption.position = "plot") +
  theme(plot.margin = margin(25, 25, 10, 25)) +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    strip.background = element_blank()
  ) +
  theme(legend.position = "top")

# Theme for the bar plots
theme_bc <- theme(
  axis.line = element_blank(),
  axis.ticks.x = element_blank(),
  axis.ticks.y = element_blank(),
  axis.text.x = element_text(color = "black"),
  panel.grid.major = element_blank(),
  panel.grid.minor = element_blank(),
  strip.background = element_blank()
)

# Custom E. color
C_E_BLUE <- "#31659f"