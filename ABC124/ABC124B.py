{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNn4rIrU2nAXg56g0cpb6wY",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC124B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1N24oNt3LviK"
      },
      "outputs": [],
      "source": [
        "n=int(input())\n",
        "h=list(map(int, input().split()))\n",
        "\n",
        "cnt=0\n",
        "for i in range(len(h)):\n",
        "  if max(h[0:i+1])==h[i]:\n",
        "    cnt+=1\n",
        "print(cnt)"
      ]
    }
  ]
}