from __future__ import annotations

from dataclasses import KW_ONLY, field
from pathlib import Path
from typing import *  # type: ignore

import rio

from .. import components as comps

class Footer(rio.Component):
    """
    A simple, static component which displays a footer with the company name and
    website name.
    """

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                rio.Image(Path(self.session.assets / "logo-transparent-white.png"), width=5, height=5),
                rio.Text("Something Fake Inc."),
                rio.Text(
                    "SUPER AWESOME WEBSITES",
                    style="dim",
                ),
                spacing=1,
                margin=2,
                align_x=0.5,
            ),
            color="hud",
            corner_radius=0,
        )

