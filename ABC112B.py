{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYNIdch/KrzGY0Z8IkwLY6",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC112B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cU6BqnzYR3CD",
        "outputId": "29d52410-75af-4fa3-d89b-4cbb4c29ca20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 70\n",
            "7 60\n",
            "1 80\n",
            "4 50\n",
            "4\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "n, b=map(int, input().split())\n",
        "\n",
        "dict = {}\n",
        "for i in range(n):\n",
        "  c, t=map(int, input().split())\n",
        "  if t <= b:\n",
        "    dict[c]=t\n",
        "\n",
        "if len(dict)==0:\n",
        "  print(\"TLE\")\n",
        "else:\n",
        "  print(min(dict))\n",
        "\n",
        "  \n",
        "\n",
        " "
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "v2yi6q58UfvR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}