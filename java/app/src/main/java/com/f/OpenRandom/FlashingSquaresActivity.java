package com.f.OpenRandom;

public class FlashingSquaresActivity {
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.widget.ImageView;

import java.util.Random;

    public class FlashingSquaresActivity extends AppCompatActivity {

        private ImageView imageView;
        private Bitmap originalBitmap;
        private Bitmap modifiedBitmap;
        private Canvas canvas;
        private Paint paint;
        private Handler handler;
        private Runnable flashRunnable;

        private int[][] squares = {
                {45, 45, 90, 90},  // Example coordinates of the first square (adjust as needed)
                // Add the coordinates for the remaining squares
        };

        private Random random = new Random();
        private int currentIndex = 0;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_flashing_squares);

            imageView = findViewById(R.id.imageView);

            originalBitmap = BitmapFactory.decodeResource(getResources(), R.drawable.PRINCESS);
            modifiedBitmap = Bitmap.createBitmap(originalBitmap.getWidth(), originalBitmap.getHeight(), Bitmap.Config.ARGB_8888);
            canvas = new Canvas(modifiedBitmap);
            paint = new Paint();

            handler = new Handler();
            flashRunnable = new Runnable() {
                @Override
                public void run() {
                    // Clear the square by drawing it with a black color
                    int[] square = squares[currentIndex];
                    int x1 = square[0];
                    int y1 = square[1];
                    int x2 = square[2];
                    int y2 = square[3];
                    paint.setColor(Color.BLACK);
                    canvas.drawRect(x1, y1, x2, y2, paint);
                    imageView.setImageBitmap(modifiedBitmap);

                    // Delay for 1 second
                    handler.postDelayed(new Runnable() {
                        @Override
                        public void run() {
                            // Restore the original content of the square
                            canvas.drawBitmap(originalBitmap, 0, 0, null);
                            imageView.setImageBitmap(modifiedBitmap);

                            // Move to the next square
                            currentIndex = (currentIndex + 1) % squares.length;

                            // Schedule the next flash
                            handler.postDelayed(this, 1000);
                        }
                    }, 1000);
                }
            };

            // Start the flashing animation
            handler.post(flashRunnable);
        }
    }

}
