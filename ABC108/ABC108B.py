{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOMswNpxe7iqi86jrgykkP3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC108B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "emSy2oKMwTuv",
        "outputId": "1f53af01-5f6f-472e-eb2e-b2676f470d9f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 0 0 1\n",
            "-1 1 -1 0\n"
          ]
        }
      ],
      "source": [
        "x1, y1, x2, y2 = map(int, input().split())\n",
        "\n",
        "x = x2-x1\n",
        "y = y2-y1\n",
        "x3 = x2 - y\n",
        "y3 = y2 + x\n",
        "x4 = x1 - y\n",
        "y4 = y1 + x\n",
        "\n",
        "print(x3, y3, x4, y4)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "mlLwrTz61Hal"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}